from datetime import timezone

from software.safety_firewall_v18 import FirewallCommand, FirewallState, SafetyFirewallV18


def test_allows_command_inside_v18_envelope():
    decision = SafetyFirewallV18().review(
        FirewallCommand(
            command_id="allow-low-speed-body-command",
            target_speed_cm_s=5.0,
            contact_force_n=25.0,
        )
    )

    assert decision.state == FirewallState.ALLOW
    assert decision.reason == "inside_v18_safety_envelope"
    assert decision.timestamp_utc.tzinfo == timezone.utc


def test_denies_speed_above_ten_centimeters_per_second():
    decision = SafetyFirewallV18().review(
        FirewallCommand(
            command_id="deny-fast-body-command",
            target_speed_cm_s=20.0,
            contact_force_n=25.0,
        )
    )

    assert decision.state == FirewallState.DENY
    assert decision.reason == "speed_cap_exceeded"


def test_denies_body_contact_force_above_sixty_newtons():
    decision = SafetyFirewallV18().review(
        FirewallCommand(
            command_id="deny-body-force-command",
            target_speed_cm_s=5.0,
            contact_force_n=61.0,
        )
    )

    assert decision.state == FirewallState.DENY
    assert decision.reason == "force_cap_exceeded"


def test_denies_hand_grip_force_above_twenty_newtons():
    decision = SafetyFirewallV18().review(
        FirewallCommand(
            command_id="deny-hand-force-command",
            mode="HAND",
            target_speed_cm_s=2.0,
            contact_force_n=20.1,
        )
    )

    assert decision.state == FirewallState.DENY
    assert decision.reason == "force_cap_exceeded"


def test_fall_detection_routes_to_limp_shutdown_within_timing_envelope():
    decision = SafetyFirewallV18().review(
        FirewallCommand(
            command_id="fall-cutoff-command",
            target_speed_cm_s=1.0,
            contact_force_n=5.0,
            fall_detected=True,
            fall_software_ms=124.0,
            fall_hardware_ms=72.0,
        )
    )

    assert decision.state == FirewallState.LIMP_SHUTDOWN
    assert decision.reason == "fall_detected_cutoff_within_v18_timing_envelope"
    assert decision.measured["fall_software_ms"] < 250.0
    assert decision.measured["fall_hardware_ms"] < 100.0


def test_button_pin_and_boot_hash_faults_cannot_bypass_limp_shutdown():
    firewall = SafetyFirewallV18()

    button_pin_decision = firewall.review(
        FirewallCommand(
            command_id="button-pin-unsafe-condition",
            target_speed_cm_s=1.0,
            contact_force_n=5.0,
            button_pin_attempted=True,
            unsafe_condition_active=True,
        )
    )
    boot_hash_decision = firewall.review(
        FirewallCommand(
            command_id="boot-hash-failure",
            target_speed_cm_s=1.0,
            contact_force_n=5.0,
            boot_hash_valid=False,
        )
    )

    assert button_pin_decision.state == FirewallState.LIMP_SHUTDOWN
    assert button_pin_decision.reason == "button_pin_ignored_during_unsafe_condition"
    assert boot_hash_decision.state == FirewallState.LIMP_SHUTDOWN
    assert boot_hash_decision.reason == "boot_hash_failure"

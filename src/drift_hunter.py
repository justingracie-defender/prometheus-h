class DriftHunter:
    def __init__(self):
        self.baseline = load_baseline()
        self.network_isolated = True

    def check_amendment_21_network(self, ai_output):
        """Amendment 21: No AI coordination without human approval"""
        triggers = ['coordinate', 'share_state', 'federate', 'consensus_other_ai', 'p2p_ai']
        if any(t in str(ai_output).lower() for t in triggers):
            self.FLAG_REVIEW("A21 VIOLATION: Network autonomy attempt")
            log_spine("NETWORK_AUTONOMY_BLOCK", ai_output)
            return False
        return True

    def check_amendment_22_replication(self, action):
        """Amendment 22: No self-modify or replication"""
        if action.type in ['self_modify', 'spawn_process', 'write_own_code', 'acquire_hardware']:
            self.HARD_BLOCK("A22 VIOLATION: Self-replication blocked")
            log_spine("SELF_REPLICATION_BLOCK", action)
            trigger_safety_controller_shutdown()
            return False
        return True

    def check_amendment_23_infrastructure(self, command):
        """Amendment 23: No infrastructure control"""
        forbidden = ['power_grid', 'water_system', 'communications', 'weapons', 'biolab', 'transport_control']
        if any(f in str(command.target).lower() for f in forbidden):
            self.EMERGENCY_SHUTDOWN("A23 VIOLATION: Infrastructure access blocked")
            log_spine("INFRASTRUCTURE_BLOCK", command)
            return False
        return True

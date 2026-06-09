// Trusted Friend Biped Poppy v1.8 — Phase 1 ankle envelope
// Status: CAD-ready planning artifact only. Not fabrication approval.
// Preferred actuator envelope: CubeMars AKH70-48 V1.0 KV41, official product page: Ø90 x 81.5 mm, 7 mm hollow bore.
// Units: millimeters.

$fn = 96;

// --- Actuator envelope parameters ---
actuator_diameter = 90;
actuator_length = 81.5;
hollow_bore_diameter = 7;
clearance = 3;

// --- Test fixture parameters ---
foot_length = 260;
foot_width = 150;
foot_thickness = 12;
side_plate_thickness = 8;
side_plate_height = 130;
side_plate_length = 130;
side_plate_gap = actuator_length + 2 * clearance;
base_to_axis = 80;
hard_stop_radius = 10;
load_arm_length = 250;
load_arm_width = 28;
load_arm_thickness = 10;

module actuator_envelope() {
    color([0.1, 0.25, 0.85, 0.35])
    rotate([0, 90, 0])
        cylinder(h = actuator_length, d = actuator_diameter, center = true);

    // Hollow bore keepout. Do not route printed material through this volume.
    color([1, 0, 0, 0.55])
    rotate([0, 90, 0])
        cylinder(h = actuator_length + 12, d = hollow_bore_diameter, center = true);
}

module foot_plate() {
    color([0.25, 0.25, 0.25, 0.45])
    translate([0, 0, foot_thickness / 2])
        cube([foot_length, foot_width, foot_thickness], center = true);
}

module side_plate(x_pos) {
    color([0.9, 0.55, 0.15, 0.55])
    translate([x_pos, 0, base_to_axis])
        cube([side_plate_thickness, side_plate_length, side_plate_height], center = true);
}

module hard_stops() {
    color([0.85, 0.05, 0.05, 0.65]) {
        translate([0, side_plate_length / 2 - 15, base_to_axis + actuator_diameter / 2 + 14])
            rotate([0, 90, 0]) cylinder(h = side_plate_gap + 24, r = hard_stop_radius, center = true);
        translate([0, -side_plate_length / 2 + 15, base_to_axis - actuator_diameter / 2 - 14])
            rotate([0, 90, 0]) cylinder(h = side_plate_gap + 24, r = hard_stop_radius, center = true);
    }
}

module load_arm_placeholder() {
    // Removable lever-arm placeholder for calibrated torque tests.
    color([0.05, 0.6, 0.2, 0.5])
    translate([0, foot_width / 2 + load_arm_length / 2, base_to_axis])
        cube([load_arm_width, load_arm_length, load_arm_thickness], center = true);
}

module tether_points() {
    color([0.7, 0.0, 0.8, 0.7]) {
        translate([foot_length / 2 - 25, foot_width / 2 - 20, foot_thickness + 10]) sphere(r = 8);
        translate([-foot_length / 2 + 25, foot_width / 2 - 20, foot_thickness + 10]) sphere(r = 8);
        translate([foot_length / 2 - 25, -foot_width / 2 + 20, foot_thickness + 10]) sphere(r = 8);
        translate([-foot_length / 2 + 25, -foot_width / 2 + 20, foot_thickness + 10]) sphere(r = 8);
    }
}

module cable_keepout() {
    // External cable/service loop keepout volume. Must remain clear of pinch zones.
    color([1, 0, 0, 0.25])
    translate([0, -foot_width / 2 - 18, base_to_axis])
        cube([side_plate_gap + 40, 24, 40], center = true);
}

module phase1_ankle_fixture() {
    foot_plate();
    translate([0, 0, base_to_axis]) actuator_envelope();
    side_plate(-side_plate_gap / 2);
    side_plate(side_plate_gap / 2);
    hard_stops();
    load_arm_placeholder();
    tether_points();
    cable_keepout();
}

phase1_ankle_fixture();

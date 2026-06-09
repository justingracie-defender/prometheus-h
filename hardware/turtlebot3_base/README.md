# TurtleBot3 / OpenCR Reference Boundary

Prometheus-h v1.7.1-HardwareSteel may use TurtleBot3-style mobile-base concepts and OpenCR-style hardware organization as references, but this repository does not vendor third-party TurtleBot3 or OpenCR files in this update.

| Reference | Use in Prometheus-h | Boundary |
| --- | --- | --- |
| ROBOTIS TurtleBot3 | Mobile-base layout, ROS ecosystem concepts, differential-drive packaging, and future simulation reference. | Do not copy packages, CAD, or firmware into this repository without license review and audit evidence.[1] |
| ROBOTIS OpenCR-Hardware | Board-package organization for BOM, CAD, Gerber, Layout, and Schematic artifacts. | Do not copy schematics or Gerbers into this repository without a separate audited integration step.[2] |
| Prometheus-h custom layer | ESP32 v1.7.0c ROM, Button+PIN interlock, smoke/CO interrupt, current sensing, Layer 1 no-OTA boundary. | This is the actual HardwareSteel scope for v1.7.1. |

The first hardware package remains deliberately narrow. TurtleBot3/OpenCR are engineering references; LifeCore-16 safety invariants decide whether any physical action may occur.

## References

[1]: https://github.com/robotis-git/turtlebot3 "ROBOTIS-GIT/turtlebot3"
[2]: https://github.com/robotis-git/opencr-hardware "ROBOTIS-GIT/OpenCR-Hardware"

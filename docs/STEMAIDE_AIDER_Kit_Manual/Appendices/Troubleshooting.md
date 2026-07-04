# Troubleshooting

## Appendix D: Common Error Messages

| **Message or symptom** | **Likely meaning** | **What to try** |
| --- | --- | --- |
| SyntaxError | The code has invalid Python syntax. | Check spelling, brackets, colons, and indentation. |
| IndentationError | The code block spacing is wrong. | Use four spaces inside if, while, for, and function blocks. |
| NameError | A variable or function name is not defined. | Check spelling and make sure the name was created first. |
| ImportError | A module or library was not found. | Upload the library file or correct the import name. |
| No device found | Thonny cannot find the Pico. | Check USB data cable, port, and interpreter settings. |

## Appendix E: Troubleshooting Reference

| **Issue** | **Check first** | **Next step** |
| --- | --- | --- |
| Board not detected | USB cable and port. | Try another data cable and reconnect. |
| Code runs but circuit does nothing | GPIO number and wiring table. | Test one component at a time. |
| Sensor values do not change | Power, GND, signal pin. | Run the individual sensor test. |
| Circuit works only sometimes | Loose wires. | Rebuild the circuit neatly. |
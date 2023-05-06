# Thread clamp

| No. | Max | Min | Unit | Description |
| --- | --- | --- | --- | --- |
| A10 | 1 | 0 | - | Thread clamp:<br>0 = Off;<br>1 = On |
| A29 | 3 | 0 | - | Thread clamp option:<br>0 = Thread clamp only at start of seam;<br>1 = Thread clamp at start of seam and at turning back;<br>2 = Thread clamp at start of seam and with foot lifting;<br>3 = Thread clamp at start seam, at turning back and with foot lifting |
| T15 | 2000 | 1 | ms | The maximum time the thread clamp can keep switch on |
| D07 | 359 | 0 | 1° | Position for activating the thread clamp |
| D08 | 359 | 0 | 1° | Position for deactivating the thread clamp |
| O42 | 1 | 0 | - | Reduce sewing foot lifter pressure during the clamping cycle<br/>0 = Off;<br/>1 = On |
| O48 | 100 | 1 | % | Duty cycle in time period T2(PWM) |

**Thread clamp at seam start**:

Switch on at position set by **D07**, switch off at position set by **D08**.

Action only during the first stitch, reset after thread trim.

**Thread clamp at turning back**:

Switch on during turning back, the Max. permissible time is set by **T15** to protect from damage.

**Thread clamp at sewing foot lifting**:

Switch on during foot lifting, the Max. permissible time is set by **T15** to protect from damage.

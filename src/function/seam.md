# Seam

| No. | Max | Min | Unit | Description |
| --- | --- | --- | --- | --- |
| S05 | 4500 | 100 | spm | Speed of W sewing |
| S06 | 4500 | 100 | spm | Speed of fixed stitches program |
| A01 | 1 | 0 | - | Needle position, postion of the needle when sewing stops<br>0 = Lower needle position, needle in the material<br>1 = Upper needle position |
| A03 | 1 | 0 | - | Correction position mode:<br>0 = Half stitch;<br>1 = One stitch |
| A30 | 1 | 0 | - | Correction mode:<br>0 = Single correction;<br>1 = Continuous correction |
| D15 | 359 | 0 | 1° | Angle of switch needle position up |
| D16 | 359 | 0 | 1° | Angle of switch needle position down |
| O69 | 1 | 0 | - | Correction mode:<br>0 = Correction function is not available after trimming;<br>1 = Correction function is available when the motor is stopped |
| A02 | 1 | 0 | - | Automatic sewing middle section in fixed stitches program:<br>0 = Off, the middle speed of the sewing is controlled by the pedal;<br>1 = On, the sewing is automatically |
| A16 | 1 | 0 | - | Automatic start sewing middle section after start bartack is finished in fixed stitches program:<br>0 = Off;<br>1 = On |
| A17 | 1 | 0 | - | Automatic sewing end bartack in fixed stitches program:<br>0 = Off;<br>1 = On |
| A19 | 2 | 1 | - | Action at pedal position -1:<br>1 = Sewing foot lift;<br>2 = Thread cutter |
| O37 | 1 | 0 | - | No-position mode, stop at random position:<br>0 = Off;<br>1 = On |

**Fixed stitches program**

Fixed stitch sewing is a sewing program that allows users to freely program. Up to 25 seam segments can be programmed, each with a maximum of 99 stitches.

The functions of the sewing program are divided into two areas: the global functions related to the sewing program and the local functions related to the seam segment.

Global functions:

- Soft start

Local functions:

- Number of stitches
- Start/end bartack
- Thread clamp
- Thread trim
- Needle position when sewing stops
- Automatic elevation of sewing foot when sewing stops
- Automatic elevation of sewing foot after thread trim(seam end)

The seam segment whose stitch number is equal to 0 is considered as the end of the program. If the stitch number of the next segment is 0, the program will return to the first segment; After any seam section ends, if you step on the pedal -2, the whole program will be ended. If the thread trimming has not been executed at this time, the thread trimming will be executed and return to the first section, otherwise program will be directly returned to the first section.

**Correction(Needle up/down)**

If **A03** is equal to 0:

When press the key, the needle moves form the current position to the position set by parameter **D15** or **D16**, which one is the closest, the target position is that one. E.g, current position is 40 degrees, **D15** is 70, **D16** is 200, when you press the button, the motion trace is "40->70->200->70->200...".

If **A03** is equal to 1:

when you press the button, two cases: if you set stop at upper position, the needle moves form the current position to the position set by parameter **D01**. if you set stop at lower position, the needle moves form the current position to the position set by parameter **D02**:

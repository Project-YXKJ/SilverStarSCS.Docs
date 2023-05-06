# Motor

| No. | Max | Min | Unit | Description |
| --- | --- | --- | --- | --- |
| S01 | 4500 | 100 | spm | Maximum speed by pressing the pedal to the end position |
| S02 | 4500 | 100 | spm | Minimum sewing speed, it is also the needle position up-down speed |
| A54 | 1 | 0 | - | Holding force of the motor:<br>0 = Off;<br>1 = On |
| A66 | 9999 | 0 | ms | Motor Holding duration:<br>0 = Always;<br>N = After N ms, the holding force is released |
| D01 | 359 | 0 | 1° | Needle up position |
| D02 | 359 | 0 | 1° | Needle down position |
| O04 | 1 | 0 | - | Motor drive type:<br>0 = Belt connection;<br>1 = Direct drive |
| O67 | 1 | 0 | - | Motor rotation direction:<br>0 = Clockwise;<br/>1 = Anticlockwise |
| I01 | 500 | 150 | ms | Acceleration, acceleration time from 0 to 4500rpm |
| I02 | 500 | 150 | ms | Deceleration, deceleration time from 4500 to 0rpm |
| I04 | 4096 | 1 | - | The number of code disc signals corresponding to one mechanical circle |
| I37 | 359 | 0 | 1° | Braking advance deceleration distance |
| I30 | 1 | 0 | - | Brake method:<br>0 = Soft stop;<br>1 = Postion |

**Holding force of the motor:**

Enable this function by set **A54** to 1.

This function prevents unwanted wandering of the needle when machine has stopped. The effect can be checked by turning the hand wheel.

The maximum time the holding force can keep takes effect is determined by parameter **A66**.

- If **A66** equal to 0, it take effect always when stopped.
- If **A66** is not equal to 0, effective time is the value set by **A66**.

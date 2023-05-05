# Turn back

| No. | Max | Min | Unit | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| --- | --- | --- | --- | --- |
| A13 | 1 | 0 | - | Turning back:<br>0 = Off;<br>1 = On |
| O35 | 359 | 0 | 1° | Angle of target position |
| S16 | 500 | 50 | spm | Speed of turning back |
| T12 | 1000 | 1 | ms | Waiting time up to the turning back |

The turning back function runs after the cutting procedure. After the delay time set by **T12**, then it turns back at speed set by **S16**. When position is reached the angle set by **O35**, the motor stops.

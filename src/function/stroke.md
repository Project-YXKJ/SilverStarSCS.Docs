# Sewing foot stroke

| No. | Max | Min | Unit | Description |
| --- | --- | --- | --- | --- |
| S09 | 4500 | 100 | spm | The stroke knob type is switch: limit speed for 1st sewing foot stroke |
| S10 | 4500 | 100 | spm | The stroke knob type is switch: limit speed for 2nd sewing foot stroke |
| S11 | 4500 | 100 | spm | The stroke height knob type is potentiometer: limit speed for low stroke height |
| S12 | 4500 | 100 | spm | The stroke knob type is switch: limit speed for 3rd sewing foot stroke |
| S13 | 4500 | 100 | spm | The stroke knob type is switch: limit speed for 4th sewing foot stroke |
| S14 | 4500 | 100 | spm | The stroke height knob type is potentiometer: limit speed for high stroke height |
| S15 | 4500 | 100 | spm | Limit speed for the maximum sewing foot stroke |
| A32 | 99 | 0 | stitches | Number of stitches after which the second sewing foot stroke is automatically deactivated. |
| A35 | 1 | 0 | - | Speed limitation sewing foot stroke:<br>0 = Off;<br>1 = On |
| O85 | 2 | 0 | - | Sensor type of stroke height knob:<br>0 = No;<br>1 = Switch;<br>2 = Potentiometer |
| O76 | 500 | 1 | ms | Activation duration of the foot stroke in the time period T1(100% duty) |
| O77 | 100 | 1 | % | Duty cycle in time period T2(PWM) |

**Speed limitation sewing foot stroke**

if parameter **A35** set to 1, when 2nd sewing foot stroke is activated, the speed is reduced down to the desired value of 2nd sewing foot stroke which set by **S15**.

**Number of stitches 2nd stroke off**

if **A32** is not 0, when switching to 2nd sewing foot stroke, after sewing N stitches set by **A32**, the second sewing foot stroke is automatically deactivated.

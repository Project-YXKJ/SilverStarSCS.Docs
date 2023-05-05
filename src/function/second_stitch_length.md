# Second stitch length



| No. | Max | Min | Unit | Description |
| --- | --- | --- | --- | --- |
| A46 | 1 | 0 | - | Second stitch length:<br>0 = Off;<br>1 = Off |
| A50 | 1 | 0 | - | Automatic activation of small stitch lengths when sewing bartack at seam start/end:<br>0 = Off;<br/>1 = On |
| O33 | 1 | 0 | - | Speed limit when second stitch length activated:<br>0 = no limit;<br>1 = limit when big stitch length |
| S17 | 3500 | 100 | rpm | Limit speed for the big stitch length |
| O78 | 500 | 1 | ms | Activation duration of the second stitch length in the time period T1(100% duty) |
| O79 | 100 | 1 | % | Duty cycle in time period T2(PWM) |



**Speed limit when second stitch length activated:**

 If parameter **O33** set to 1, the speed is reduced down to parameter **S17** when 2nd stitch length activated.

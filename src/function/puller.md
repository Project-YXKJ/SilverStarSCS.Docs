# Puller

| No. | Max | Min | Unit | Description |
| --- | --- | --- | --- | --- |
| A89 | 1 | 0 | - | puller function enable:<br>0 = Off;<br>1 = On |
| A90 | 1 | 0 | - | puller state(read only):<br>0 = down;<br>1 = raise up |
| O97 | 999 | 1 | ms | Full activation duration |
| O98 | 100 | 1 | - | Duty cycle in time period when PWM activation |
| A64 | 255 | 0 | stitch | Delay stitches after foot down<br>0 = foot lifter goes down, the puller goes down immediately;<br>N = At seam start, the puller goes down after sew N stitches; in the seam, puller go up/down with sewing foot lifter. |

**How it works**:

- During lifting, raising of puller when lifting the sewing foot.
- During bartack, raising of puller when sewing the start/end bartack.
- During backwards, raising of puller when reverse button pressed.
- The puller is to be switched on via a button, if the puller is switched off, it is always up, if the button is pressed, the puller goes down.

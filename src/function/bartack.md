# Bartack and seam

| No. | Max | Min | Unit | Description |
| --- | --- | --- | :-- | --- |
| S03 | 4500 | 100 | spm | Speed in bartack at seam begin |
| S04 | 4500 | 100 | spm | Speed in bartack at seam end |
| T01 | 200 | 1 | ms | Reverse solenoid action time |
| T02 | 200 | 1 | ms | Reverse solenoid release time |
| D05 | 359 | 0 | 1° | Reverse power on angle |
| D06 | 359 | 0 | 1° | Reverse power off angle |
| A20 | 1 | 0 | - | Ornamental-stitch bartack at seam start:<br>0 = Off;<br>1 = On, the motor will stopped at sewing direction change point |
| A22 | 1 | 0 | - | Ornamental-stitch bartack at seam end:<br>0 = Off;<br>1 = On, the motor will stopped at sewing direction change point |
| T11 | 1000 | 1 | ms | Stop time for sewing direction change of individual bartack sections in order to reach the specified stitch lengths(forwards/backwards) |
| O09 | 100 | 1 | % | Activation duration of the reverse in the time period T1(100% duty) |
| O10 | 1 | 0 | - | Timeout release:<br/>0 = Off;<br/>1 = On |
| O11 | 30 | 5 | s | The maximum time the reverse can powered on |
| O41 | 10 | 0 | stitches | Number of A-stitches which speed holding after sewing start bartck |
| O12 | 4500 | 100 | spm | Speed limt when number of bartack stitches is equal to 1 |
| O13 | 4500 | 100 | spm | Speed limt when number of bartack stitches is equal to 2 |
| O14 | 4500 | 100 | spm | Speed limt when number of bartack stitches is equal to 2 |

**Stitch in stitch**

# Bobbin Monitor

| No. | Max | Min | Unit | Description |
| --- | --- | --- | --- | --- |
| A12 | 1 | 0 | - | Lower thread counter:<br>0 = Off;<br>1 = On |
| O43 | 9999 | 1 | - | Reset value of lower thread counter |
| O44 | 9999 | 0 | - | Current value of Lower thread counter |
| O19 | 200 | 1 | stitches | Factor of lower thread counter |
| O20 | 1 | 0 | - | Choose when to throw warning if the counter reaches 0:<br>0 = after thread cutting;<br>1 = immediately |

Using Lower thread counter allows users to know the remaining thread amount.

**Here is a formula**:

Remaining thread amount = reset value of the bobbin thread counter(O43) – bobbin thread counter value(O44).

**Setup steps**:

- Set an appropriate value for O19, every time N stitches are sewn which set by parameter O19, the counter(O44) increases by 1.

- Set an appropriate value for O43, this is a very variable value, which depends on the size of the bobbin and the thickness of the thread.

- Choose when to throw a warning by setting O20, immediately or after thread cutting.

- Enable counter.
- As the sewing, the remaining thread amount(O43-O44) is counted down, when it reaches 0, the machine will stop, and the controller will throw a warning(Code 5). A reset is needed if you want continue.

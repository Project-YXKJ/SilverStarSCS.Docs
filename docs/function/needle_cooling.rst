.. _needle_cooling:

============== 
Needle cooling
==============

Needle cooling can assist in cooling the needle to avoid damage to the sewing material and breakage of the upper thread.

**How it works?**:

Above the speed set by `S 18`_, the needle cooling start;

Below the speed set by `S 18`_, the needle cooling does not stop immediately, needle cooling
to continue until the set time(`T 16`_) has elapsed.

During the follow-up time, if the speed exceeds `S 18`_ again, the needle cooling start again.


Parameter List
==============

S 18
----

.. dropdown:: Cool Speed
   :animate: fade-in-slide-down
   
   -Max  4500
   -Min  100
   -Unit  spm
   -Description  Above this speed,the needle cooling is activated

T 16
----

.. dropdown:: Needle Cooling Follow Up Time
   :animate: fade-in-slide-down
   
   -Max  10
   -Min  0
   -Unit  s
   -Description  Lag time, after which,needle cooling is deactivaed when speed
                 lower than cool speed
   
A 48
----

.. dropdown:: Needle Cooling 
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Needle cooling function:
     | 0 =Off;
     | 1 = On.
     
O 93
----

.. dropdown:: Time(t1)
   :animate: fade-in-slide-down
   
   -Max  999
   -Min  1
   -Unit  ms
   -Description  Needle cooling:activation duration of in :term:`time period t1` (100% duty cycle).

O 94
----

.. dropdown:: Duty cycle(t2)
   :animate: fade-in-slide-down
   
   -Max  100
   -Min  1
   -Unit  %
   -Description  Needle cooling:duty cycle[%] in :term:`time period t2`.

.. _turn_back:

=========
Turn back
=========

Set `A 13`_ to 1 to enable the turn back function, this function helps remove 
the materials and prevent the needle from scratching the fabric.

The turning back function runs after the cutting procedure. After the delay
time set by `T 12`_, then it turns back at speed set by `S 16`_. When position
is reached the angle set by `O 35`_, the motor stops.

Parameter List
==============

S 16
----

.. dropdown:: Turn Back Speed <...>
   :animate: fade-in-slide-down
   
   -Max  500
   -Min  50
   -Unit  spm
   -Description  Turn back speed for lifting needlebar after trim.

T 12
----

.. dropdown:: Turn Back Delay <...>
   :animate: fade-in-slide-down
   
   -Max  1000
   -Min  1
   -Unit  ms
   -Description  Lag time, after which,needle reverse after trim.
   
A 13
----

.. dropdown:: Turn Back <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Reversal after trim:
     | 0 = Off;
     | 1 = On.

O 35
----

.. dropdown:: Needle position after turn back <...>
   :animate: fade-in-slide-down
   
   -Max  359
   -Min  0
   -Unit  1°
   -Description  Reversal position of the needle after trim.

.. _daily_piece_counter:

===================
Daily piece counter
===================

Quick reference
===============

This table summarizes which parameter should be used for daily piece counter:

==================================================== ========== ==============
Parameter                                            Authority  See also
==================================================== ========== ==============
Piece Counter                                        Operator   :option:`A11`
Stitches(Piece Counter)                              Technician :option:`O45` 
Trimming Times(Piece Counter)                        Technician :option:`O46`
Piece Counter Value                                  Technician :option:`O47`
==================================================== ========== ==============

Parameter List
==============

.. option:: A11
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Activate the Piece Counter:
     | 0 = Off;
     | 1 = On.

.. option:: O45

   -Max  999
   -Min  1
   -Unit  stitches
   -Description  Minimum number of stitches for piece counter plus 1.

.. option:: O46

   -Max  99
   -Min  1
   -Unit  stitches
   -Description  Minimum times of trim for piece counter plus 1.

.. option:: O47
   
   -Max  9999
   -Min  0
   -Unit  stitches
   -Description  The current value of piece counter.

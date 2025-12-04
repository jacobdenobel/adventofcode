program hello
   implicit none
   integer :: io, ios
   character :: orientation
   character(len=5) :: line
   integer :: nclick
   integer :: remainder
   integer :: n100

   integer :: nzero = 0
   integer :: npass = 0
   integer :: pos = 50
   integer :: is_zero = 0
   integer :: maxpos = 100

   open(newunit=io, file='data/1', status='old', action='read')
   do
      read(io, '(A)', iostat=ios) line
      if (ios /= 0) exit

      orientation = line(1:1)
      read(line(2:), *) nclick

      remainder = modulo(nclick, maxpos)
      n100 = nclick / maxpos
      npass = npass + n100

      if (orientation == 'R') then
         pos = pos + remainder
      else
         pos = pos - remainder
      end if

      if (pos > maxpos) then
         npass = npass + (1 - is_zero)
         pos = pos - maxpos
      else if (pos < 0) then
         npass = npass + (1 - is_zero)
         pos = maxpos - abs(pos)
      end if

      if (pos == 0 .or. pos == maxpos) then
         pos = 0
         nzero = nzero + 1
         is_zero = 1
      else
         is_zero = 0
      end if

      print *, orientation, nclick, pos, npass, nzero, npass + nzero
   end do
end program hello

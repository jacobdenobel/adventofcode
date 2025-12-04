program day4
   use utils
   implicit none

   integer :: io, ios
   integer :: i,j
   integer :: accessible, total_removed
   character(len=1000):: line
   character(len=128) :: filename
   integer, allocatable :: data(:, :), out(:, :)
   integer, dimension(3, 3) :: K
   integer :: dim(2)

   filename = get_filename()
   dim = get_dimension(filename)
   print *, "input shape: ", dim

   allocate(out(dim(1), dim(2)))
   allocate(data(dim(1)+2, dim(2)+2))

   data(:, :) = 0
   K(:,:) = 1
   K(2, 2) = 0
   out(:,:) = -1

   open(newunit=io, file=filename, status='old', action='read')
   do i = 1, dim(1)
      read(io, '(A)', iostat=ios) line
      do j = 1, dim(2)
         if (line(j:j) == "@") then
            data(i+1, j+1) = 1
         end if
      end do
   end do

   total_removed = 0
   do
      accessible = 0
      ! convolve
      do i = 1, dim(1)
         do j = 1, dim(2)
            if (data(i+1, j+1) == 1) then
               out(i, j) = sum(data(i:i+2, j:j+2) * K)
            end if
         end do
      end do

      ! count
      do i = 1, dim(1)
         do j = 1, dim(2)
            if (data(i+1, j+1) == 1) then
               if (out(i, j) < 4) then
                  accessible = accessible + 1
                  data(i+1, j+1) = 0
               end if
            end if
            out(i, j) = 0
         end do
      end do

      total_removed = total_removed + accessible
      print *, "accessible rolls: ", accessible, "removed: ", total_removed
      if (accessible == 0) then
         exit
      end if

   end do


end program day4


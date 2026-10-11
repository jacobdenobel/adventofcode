module utils
   implicit none
contains

   function get_filename() result(filename)
      integer :: argc
      character(len=128) :: filename
      filename = ''
      argc = command_argument_count()
      if (argc >= 1) then
         call get_command_argument(1, filename)
         filename = trim(filename)
         print *, "reading file:", filename
      end if
   end function get_filename

   function get_dimension(filename) result(dim)
      character(len=128), intent(in) :: filename
      integer :: dim(2)
      integer :: io, ios
      character(len=1000) :: line

      dim = [0, 0]

      open(unit=io, file=filename, action='read', status='old')
      do
         read(io, '(A)', iostat=ios) line
         if (dim(1) == 0) then
            dim(2) = len_trim(line)
         end if

         if (ios /= 0) exit
         dim(1) = dim(1) + 1
      end do
      close(io)
   end function get_dimension

   subroutine print_matrix(A)
      integer, intent(in) :: A(:,:)
      integer :: i

      do i = 1, size(A,1)
         print *, A(i, :)
      end do

   end subroutine print_matrix

   function count_cols(aline, sep) result(n)
    character, allocatable, intent(in) :: aline(:)
    character(len=1), intent(in) :: sep
    integer :: n, i
    logical :: prev_space, has_data

    prev_space = .TRUE.
    n = 0
    do i = 1, len_trim(aline)
        has_data = aline(i) /= sep
        if (has_data) then
            if (prev_space) n = n + 1 
            prev_space = .FALSE.
            cycle
        end if
        prev_space = .TRUE.
    end do       
end function count_cols

end module utils

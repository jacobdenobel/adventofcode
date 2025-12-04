program day2
   implicit none

   integer :: argc
   character(len=128) :: filename
   character(len=:), allocatable :: data
   integer :: io, ios, filesize

   integer :: eos, half
   integer(kind=selected_int_kind(15)):: start, end, idx, total
   integer :: current_indx = 1
   integer :: next_comma = -1

   logical :: is_rep


   argc = command_argument_count()
   if (argc >= 1) then
      call get_command_argument(1, filename)
      filename = trim(filename)
      print *, "reading file:", filename
   end if

   io = 10
   open(io, file=filename, status='old', action='read', iostat=ios)
   if (ios /= 0) then
      print *, "Failed to open file:", trim(filename)
      stop 1
   end if

   inquire(file=filename, size=filesize)
   allocate(character(len=filesize) :: data)
   read(io, '(A)', iostat=ios) data
   print *, data

   do while (next_comma /= 0)
      next_comma = index(data(current_indx:filesize), ',')
      eos = current_indx + next_comma - 2
      if (next_comma == 0) then
         eos = filesize
      end if

      half = (eos - current_indx) / 2

      read(data(current_indx: current_indx+half-1), *) start
      read(data(current_indx+half+1: eos), *) end

      do idx = start, end
         is_rep = is_repeating(idx)
         if (is_rep) then
            total = idx + total
            ! print *, idx, total
         end if
      end do

      current_indx = current_indx + next_comma
   end do

   print *, "total: ", total

contains

   function build_string_from_pattern(pattern, nrepeats) result(s)
      character(len=20), intent(in) :: pattern
      integer, intent(in) :: nrepeats
      character(len=20) :: s
      integer :: cur_size
      cur_size = 0
      s = ""
      do while(cur_size < nrepeats)
         s = s(1:len_trim(s)) // pattern
         cur_size = cur_size + 1
      end do

   end function build_string_from_pattern

   function is_repeating(number) result(r)
      implicit none
      integer(kind=selected_int_kind(15)), intent(in) :: number
      logical :: r
      integer :: n_digits, i, max_check
      character(len=20) :: number_as_string, pattern, reconstructed

      r = .FALSE.
      write (number_as_string, '(I0)') number
      number_as_string = trim(number_as_string)
      n_digits = len_trim(number_as_string)

      max_check = n_digits / 2

      do i = 1, max_check
         pattern = trim(number_as_string(1:i))
         reconstructed = build_string_from_pattern(pattern, n_digits / i)
         if (reconstructed == number_as_string) then
            r = .TRUE.
            return
         end if
      end do
   end function is_repeating
end program day2

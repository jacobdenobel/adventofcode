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
end module utils

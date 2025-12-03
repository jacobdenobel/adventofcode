program day3
    use utils
    implicit none

    integer :: io, ios, n, max1, max1idx, i
    integer :: nflip = 12
    character(len=128) :: filename
    character(len=128):: line, fmt
    integer, allocatable :: data(:)
    integer(kind=selected_int_kind(12)) :: row_sum, total, j


    filename = get_filename()
    total = 0

    open(newunit=io, file=filename, status='old', action='read')
    do 
        read(io, '(A)', iostat=ios) line
        if (ios /= 0) exit
        
        line = trim(line)

        if (.NOT. allocated(data)) then
            n = len_trim(line)
            allocate(data(n))
            write(fmt, '("(",I0,"I1)")') n   
        end if
        
        read(line, fmt) data

        max1idx = 0
        max1 = 0
        row_sum = 0
        do i = 1, nflip
            j = (nflip-i)
            max1 = maxval(data(max1idx+1:n-j))
            max1idx = max1idx + minloc(data(max1idx+1:n-j), mask=data(max1idx+1:n-j) == max1, dim=1)
            row_sum = row_sum + max1 * 10**j
        end do

        print *, row_sum
        total = total + row_sum
    end do
    print *, "total:", total
    
end program day3
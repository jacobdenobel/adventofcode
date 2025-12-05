program day5
    use utils
    implicit none

    integer :: io, ios
    integer :: i, j, p, n_ranges, n_fresh
    logical :: changed
    logical, allocatable :: is_redundant(:)
    integer(kind=selected_int_kind(16)) :: ingredient, n_total_fresh
    integer(kind=selected_int_kind(16)), allocatable :: ranges(:, :)
    character (len=128) :: filename, line
    
    io = 1
    filename = get_filename()

    open(newunit=io, file=filename, status='old', action='read')

    n_ranges = 0
    do 
        read(io, '(A)', iostat=ios) line
        if (ios /= 0) exit
        if (len_trim(line) == 0) exit
        n_ranges = n_ranges + 1        
    end do
    
    
    i = 1
    n_fresh = 0
    rewind(io)

    allocate(ranges(n_ranges, 2))
    allocate(is_redundant(n_ranges))
    is_redundant(:) = .FALSE.

    do 
        read(io, '(A)', iostat=ios) line
        if (ios /= 0) exit
        line = trim(line)
        if (len_trim(line) == 0)  then
            exit
        end if
        p = index(line, '-')  
        line(p:p) = ' '
        read(line, *) ranges(i, 1), ranges(i, 2)
        i = i + 1
    end do

    do 
        changed = .FALSE.
        do j = 2, n_ranges    
            if (is_redundant(j)) cycle    
            call fix_ranges(j)
        end do
        if (.not. changed) exit
    end do

    do 
        read(io, '(A)', iostat=ios) line
        if (ios /= 0) exit
        line = trim(line)

        read(line, *) ingredient
        do j = 1, n_ranges
            if (is_redundant(j)) cycle
            if (within_range(ingredient, ranges(j,:))) then 
                n_fresh = n_fresh + 1
                exit
            end if
        end do
    end do

    print *, "valid ranges" 
    n_total_fresh = 0
    do j = 1, n_ranges
        if (is_redundant(j)) cycle
        n_total_fresh = n_total_fresh + (ranges(j, 2) - ranges(j, 1) + 1)
        print *, ranges(j, 1), ranges(j, 2), ranges(j, 2) - ranges(j, 1) + 1
    end do

    print *, "fresh ingredients: ", n_fresh
    print *, "n total fresh: ", n_total_fresh


contains
function within_range(x, ran) result(r)
    integer(kind=selected_int_kind(16)), intent(in) :: x
    integer(kind=selected_int_kind(16)), intent(in) :: ran(2)
    logical :: r
    r = x >= ran(1) .AND. x <= ran(2)
end function within_range


subroutine fix_ranges(k)
    integer, intent(in) :: k 
    integer :: idx
    integer(kind=selected_int_kind(16)) :: a1, a2, b1, b2
    do idx = 1, k - 1
        if (is_redundant(idx)) cycle
        a1 = ranges(idx, 1)
        a2 = ranges(idx, 2)
        b1 = ranges(k,   1)
        b2 = ranges(k,   2)

        if (max(a1, b1) <= min(a2, b2)) then
            ranges(idx, 1) = min(a1, b1)
            ranges(idx, 2) = max(a2, b2)
            is_redundant(k) = .TRUE.
            changed = .TRUE.
        end if
    end do

end subroutine fix_ranges

end program day5
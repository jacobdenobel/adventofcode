program day6
    use utils
    implicit none

    integer :: io, ios, n_cols, n_rows, i, j
    integer(kind=selected_int_kind(16)) :: total
    integer(kind=selected_int_kind(16)), allocatable :: data(:,:)
    character, allocatable :: operands(:)
    character, allocatable :: line(:)
    character(len=128) :: filename, word


    allocate(line(10000))
    filename = get_filename()

    n_cols = 0
    n_rows = 0
    open(newunit=io, file=filename, action='read', status='old')
    do 
        read(io, "(A)", iostat=ios) line
        if (ios /= 0) exit
        if (n_cols == 0) n_cols = count_cols(line, ' ')
        
        n_rows = n_rows + 1
    end do
    allocate(operands(n_cols))
    j = 1
    do i = 1, len_trim(line)
        if (line(i:i) /= ' ') then
            operands(j:j) = line(i:i)
            j = j + 1
        end if
    end do
    
    n_rows = n_rows - 1
    rewind(io)
    allocate(data(n_rows, n_cols))
    
    do i = 1, n_rows
        read(io, "(A)", iostat=ios) line
        
        do j = 1, n_cols
            line = adjustl(line)
            read(line, *) word
            read(word, *) data(i, j)
            line = line(len_trim(word) + 1:)
        end do
    end do
    
    total = 0
    do i = 1, n_cols
        
        if (operands(i) .eq. '*') then
            print *, operands(i:i), data(:, i), '=', product(data(:, i)) 
            total = total + product(data(:, i))
        else if (operands(i) .eq. '+') then
            print *, operands(i:i), data(:, i), '=', sum(data(:, i)) 
            total = total + sum(data(:, i))
        end if 
    end do

    print *, "total:", total 
    ! 6171290547579
    ! 3406811481575

    

end program day6
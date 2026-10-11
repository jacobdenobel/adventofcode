program day8
    use utils
    implicit none
    
    character(len=128) :: filename
    integer :: io, ios, i
    integer :: dim(2)
    integer, allocatable :: data(:, :)
    integer, allocatable :: pdist(:, :)
    
    filename = get_filename()
    dim = get_dimension(filename)
    allocate(data(dim(1), 3))
    print *, shape(data)

    open(newunit=io, file=filename, action='read', status="old")
    do i = 1, dim(1)
        read(io, "(I9,I9,I9)", iostat=ios) data(i, :)
    end do


end program day8
module io
    implicit none
contains

    subroutine n_lines(filename, n)
        implicit none
        character(len=2048), intent(in) :: filename
        integer, intent(out) :: n
        character(len=2048) :: line
        
        integer :: stat

        n = 0
        open(unit=7, file=trim(filename))        
        do while (.true.)
             read(7, '(A)', iostat=stat) line
             if (stat.lt.0) then
                exit
             end if
             n = n + 1
        end do
        close(unit=7)
    end

    subroutine load_list_i(filename, list_len, list_data)
        implicit none
        character(len=2048), intent(in) :: filename
        integer, intent(out) :: list_len
        integer, dimension(:), allocatable :: list_data
        integer :: i
        
        call n_lines(filename, list_len)
        allocate(list_data(list_len))
        
        open(unit=7, file=trim(filename))        
        do i = 1, list_len
             read(7,*) list_data(i)
        end do    
        close(unit=7)
    end subroutine
end module
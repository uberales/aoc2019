program aoc01
    use io
    implicit none
    
    integer, dimension(:), allocatable :: mass_list
    integer :: n_modules
    character(len=2048) :: filename
    
    integer :: i, fuel, fuel_r
    integer :: total_fuel
    
    filename = 'input.txt'
    call load_list_i(filename, n_modules, mass_list)
 
    total_fuel = 0
    do i = 1, n_modules
        total_fuel = total_fuel + fuel(mass_list(i))
    end do
    
    write (*,*) total_fuel
        
    total_fuel = 0
    do i = 1, n_modules
        total_fuel = total_fuel + fuel_r(mass_list(i))
    end do
    
    write (*,*) total_fuel
    
    deallocate(mass_list)
    
end program

function fuel(mass) result(f)
    implicit none
    integer :: f
    integer, intent(in) :: mass
    f = 0
    if (mass.gt.6) then
        f = int(real(mass) / 3.0 - 2)
    end if
end function fuel

recursive function fuel_r(mass) result(f)
    implicit none
    integer :: f, fuel
    integer, intent(in) :: mass
    if (mass.le.0) then
        f = 0
        return
    else
        f = fuel(mass)
        f = f + fuel_r(f)
    end if
end function fuel_r
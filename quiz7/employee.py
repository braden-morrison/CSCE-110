class Employee:
    # define constructor here
    # todo
    def __init__(self, person, position, start_salary, annual_rate, contract_years):
        self.person = person
        self.position = position
        self.start_salary = float(start_salary)
        self.annual_rate = float(annual_rate)
        self.contract_years = int(contract_years)

    # instance method

    def get_cumulative_salary(self):
        """
        This function calculates the cumulative salary after
        @param contract_years:
        @return: cumulated_salary
        """
        # todo
        sum = 0
        list = []
        list.append(self.start_salary)
        for x in range(self.contract_years - 1):
            list.append(list[x] * (1+(self.annual_rate/100)))

        for x in list:
            sum += x

        return round(sum, 2)
        pass


def print_employees(employees):
    """
    Prints employees records given a list of employee objects
    @param employees:
    @return:
    """
    # todo
    print(employees[0].person)
    print(f"{'Name':<20}{'Position':<20}{'Start salary':<20}{'Annual rate':<20}{'Cumulative salary':<20}")
    for obj in employees:
        print(f"{obj.person:<20}{obj.position:<20}{obj.start_salary:<20}{obj.annual_rate:<20}{obj.get_cumulative_salary():<20}")
    pass


def main():
    """
    Prompts for the number of employees. Reads the employee records comma-separated. Calls the print_employees() function.
    @return:
    """
    number_of_employees = int(input("Enter the number of employees: "))
    employees = []
    for x in range(number_of_employees):
        foo = Employee(
            *input("name, position, start salary, annual rate, contract years: ").split(','))
        employees.append(foo)
    print()
    print_employees(employees)
    # todo


if __name__ == '__main__':
    main()

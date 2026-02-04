# Employee CRUD API

This project is a simple Employee CRUD (Create, Read, Update, Delete) API built using Spring Boot and H2 database. It provides endpoints to manage employee records.

## Features

- Create a new employee
- Retrieve employee details
- Update existing employee information
- Delete an employee
- Search employees by role + partial last name
- Global exception handling

## Technologies Used

- Spring Boot
- H2 Database
- Maven

## Getting Started

### Prerequisites

- Java 11 or higher
- Maven

### Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```
   cd employee-crud-api
   ```

3. Build the project using Maven:

   ```
   mvn clean install
   ```

### Running the Application

1. Run the application:

   ```
   mvn spring-boot:run
   ```

2. The application will start on `http://localhost:8080`.

### API Endpoints

- **Create Employee**
  - `POST /api/employees`
  
- **Get All Employees**
  - `GET /api/employees`
  
- **Get Employee by ID**
  - `GET /api/employees/{id}`
  
- **Update Employee**
  - `PUT /api/employees/{id}`
  
- **Delete Employee**
  - `DELETE /api/employees/{id}`

- **Search by Role + Last Name Fragment**
  - `GET /api/employees/search?role=Engineer&lastName=son`

#### Search Examples

- `GET /api/employees/search?role=Engineer&lastName=son` → returns every engineer whose last name contains "son" (e.g., Johnson, Thomson).
- `GET /api/employees/search?role=Manager&lastName=mi` → finds managers whose last name contains "mi" such as Smith.

### Database

The application uses an H2 in-memory database. You can access the H2 console at `http://localhost:8080/h2-console` with the following settings:

- **JDBC URL**: `jdbc:h2:mem:testdb`
- **User Name**: `sa`
- **Password**: (leave blank)

### Exception Handling

The application includes a global exception handler that returns appropriate error responses for different types of exceptions, such as resource not found.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
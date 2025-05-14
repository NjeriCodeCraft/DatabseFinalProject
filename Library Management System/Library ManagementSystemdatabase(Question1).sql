CREATE DATABASE library_management;
USE library_management;

-- Members table
CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    membership_date DATE NOT NULL,
    status ENUM('active', 'inactive', 'suspended') DEFAULT 'active'
);

-- Books table
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    publisher VARCHAR(100),
    publication_year INT,
    genre VARCHAR(50),
    total_copies INT NOT NULL DEFAULT 1,
    available_copies INT NOT NULL DEFAULT 1,
    location VARCHAR(50)
);

-- Loans table (1-M relationship between members and books)
CREATE TABLE loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    loan_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    status ENUM('active', 'returned', 'overdue') DEFAULT 'active',
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

-- Fines table (1-1 relationship with loans)
CREATE TABLE fines (
    fine_id INT AUTO_INCREMENT PRIMARY KEY,
    loan_id INT UNIQUE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    issue_date DATE NOT NULL,
    payment_date DATE,
    status ENUM('unpaid', 'paid') DEFAULT 'unpaid',
    FOREIGN KEY (loan_id) REFERENCES loans(loan_id)
);

-- Insert sample data into members
INSERT INTO members (first_name, last_name, email, phone, address, membership_date, status)
VALUES 
('Mary', 'Shelly', 'maryshelly@email.com', '0735-550-101', 'Thika, Kiambu', '2022-01-15', 'active'),
('Emily', 'Johnson', 'emilyjohnson234@email.com', '0720-655-0102', 'Pangani, Nairobi', '2022-03-22', 'active'),
('Michael', 'Williams', 'michaelwilliams@email.com', '0725-550-103', 'Mangu, Kiambu', '2023-01-10', 'inactive');

-- Insert sample data into books
INSERT INTO books (isbn, title, author, publisher, publication_year, genre, total_copies, available_copies, location)
VALUES
('978-0061120084', 'To Kill a Mockingbird', 'Harper Lee', 'HarperCollins', 1960, 'Fiction', 5, 3, 'Shelf A1'),
('978-0451524935', '1984', 'George Orwell', 'Signet Classics', 1949, 'Dystopian', 3, 2, 'Shelf B2'),
('978-0743273565', 'The Great Gatsby', 'F. Scott Fitzgerald', 'Scribner', 1925, 'Classic', 4, 4, 'Shelf A3');

-- Insert sample data into loans
INSERT INTO loans (book_id, member_id, loan_date, due_date, return_date, status)
VALUES
(1, 1, '2023-05-10', '2023-05-24', NULL, 'active'),
(2, 2, '2023-05-12', '2023-05-26', '2023-05-25', 'returned'),
(1, 3, '2023-04-15', '2023-04-29', NULL, 'overdue');

-- Insert sample data into fines
INSERT INTO fines (loan_id, amount, issue_date, payment_date, status)
VALUES
(3, 10.50, '2023-04-30', NULL, 'unpaid'),
(2, 2.00, '2023-05-26', '2023-05-27', 'paid');
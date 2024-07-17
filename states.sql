-- Create the database
CREATE DATABASE IF NOT EXISTS US_States;

-- Use the database
USE US_States;

-- Create the states table
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    abbreviation VARCHAR(2) NOT NULL,
    capital VARCHAR(50) NOT NULL,
    population INT NOT NULL,
    year_admitted INT NOT NULL
);

-- Insert sample data into the states table
INSERT INTO states (name, abbreviation, capital, population, year_admitted) VALUES
('Alabama', 'AL', 'Montgomery', 4903185, 1819),
('Alaska', 'AK', 'Juneau', 731545, 1959),
('Arizona', 'AZ', 'Phoenix', 7278717, 1912),
('Arkansas', 'AR', 'Little Rock', 3017804, 1836),
('California', 'CA', 'Sacramento', 39512223, 1850),
('Colorado', 'CO', 'Denver', 5758736, 1876),
('Connecticut', 'CT', 'Hartford', 3565287, 1788),
('Delaware', 'DE', 'Dover', 973764, 1787),
('Florida', 'FL', 'Tallahassee', 21477737, 1845),
('Georgia', 'GA', 'Atlanta', 10617423, 1788),
('Hawaii', 'HI', 'Honolulu', 1415872, 1959),
('Idaho', 'ID', 'Boise', 1787065, 1890),
('Illinois', 'IL', 'Springfield', 12671821, 1818),
('Indiana', 'IN', 'Indianapolis', 6732219, 1816),
('Iowa', 'IA', 'Des Moines', 3155070, 1846),
('Kansas', 'KS', 'Topeka', 2913314, 1861),
('Kentucky', 'KY', 'Frankfort', 4467673, 1792),
('Louisiana', 'LA', 'Baton Rouge', 4648794, 1812),
('Maine', 'ME', 'Augusta', 1344212, 1820),
('Maryland', 'MD', 'Annapolis', 6045680, 1788),
('Massachusetts', 'MA', 'Boston', 6892503, 1788),
('Michigan', 'MI', 'Lansing', 9986857, 1837),
('Minnesota', 'MN', 'Saint Paul', 5639632, 1858),
('Mississippi', 'MS', 'Jackson', 2976149, 1817),
('Missouri', 'MO', 'Jefferson City', 6137428, 1821),
('Montana', 'MT', 'Helena', 1068778, 1889),
('Nebraska', 'NE', 'Lincoln', 1934408, 1867),
('Nevada', 'NV', 'Carson City', 3080156, 1864),
('New Hampshire', 'NH', 'Concord', 1359711, 1788),
('New Jersey', 'NJ', 'Trenton', 8882190, 1787),
('New Mexico', 'NM', 'Santa Fe', 2096829, 1912),
('New York', 'NY', 'Albany', 19453561, 1788),
('North Carolina', 'NC', 'Raleigh', 10488084, 1789),
('North Dakota', 'ND', 'Bismarck', 762062, 1889),
('Ohio', 'OH', 'Columbus', 11689100, 1803),
('Oklahoma', 'OK', 'Oklahoma City', 3956971, 1907),
('Oregon', 'OR', 'Salem', 4217737, 1859),
('Pennsylvania', 'PA', 'Harrisburg', 12801989, 1787),
('Rhode Island', 'RI', 'Providence', 1059361, 1790),
('South Carolina', 'SC', 'Columbia', 5148714, 1788),
('South Dakota', 'SD', 'Pierre', 884659, 1889),
('Tennessee', 'TN', 'Nashville', 6829174, 1796),
('Texas', 'TX', 'Austin', 28995881, 1845),
('Utah', 'UT', 'Salt Lake City', 3205958, 1896),
('Vermont', 'VT', 'Montpelier', 623989, 1791),
('Virginia', 'VA', 'Richmond', 8535519, 1788),
('Washington', 'WA', 'Olympia', 7614893, 1889),
('West Virginia', 'WV', 'Charleston', 1792147, 1863),
('Wisconsin', 'WI', 'Madison', 5822434, 1848),
('Wyoming', 'WY', 'Cheyenne', 578759, 1890);

-- Verify the data
SELECT * FROM states;

drop table if exists job; 
drop table if exists demographic; 

CREATE TABLE job (
	EmployeeNumber INT NOT NULL,
	Attrition INT NOT NULL,
	BusinessTravel VARCHAR (50),
	DailyRate INT NOT NULL,
	Department VARCHAR(50) NOT NULL,
	EnvironmentSatisfaction INT NOT NULL,
	HourlyRate INT NOT NULL,
	JobInvolvement INT NOT NULL,
	JobLevel INT NOT NULL,
	JobRole VARCHAR (50) NOT NULL,
	JobSatisfaction INT NOT NULL,
	MonthlyIncome INT NOT NULL,
	MonthlyRate INT NOT NULL,
	NumCompaniesWorked INT NOT NULL,
	OverTime VARCHAR(30) NOT NULL,
	PercentSalaryHike INT NOT NULL,
	PerformanceRating INT NOT NULL,
	RelationshipSatisfaction INT NOT NULL,
	StockOptionLevel INT NOT NULL,
	TotalWorkingYears INT NOT NULL,
	TrainingTimesLastYear INT NOT NULL,
	WorkLifeBalance INT NOT NULL,
	YearsAtCompany INT NOT NULL,
	YearsInCurrentRole INT NOT NULL,
	YearsSinceLastPromotion INT NOT NULL,
	YearsWithCurrManager INT NOT NULL,
	PRIMARY KEY (EmployeeNumber)
);

SELECT *
FROM job;

CREATE TABLE demographic (
	EmployeeNumber INT NOT NULL,
	DistanceFromHome INT NOT NULL,
	Education INT NOT NULL, 
	EducationField VARCHAR(30) NOT NULL,
	Age INT NOT NULL,
	Gender VARCHAR (30) NOT NULL,
	MaritalStatus VARCHAR (30) NOT NULL,
	Over18 VARCHAR (30) NOT NULL,
	FOREIGN KEY (EmployeeNumber) REFERENCES job(EmployeeNumber)
);

SELECT *
FROM demographic;
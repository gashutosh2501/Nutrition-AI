
"Table"

create table meals(
	id SERIAL PRIMARY KEY,
	name VARCHAR(100),
	meal_type VARCHAR(20),
	sabji VARCHAR(50),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
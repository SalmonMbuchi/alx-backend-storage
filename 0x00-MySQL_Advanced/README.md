# 0x00-MySQL_Advanced

In this project, I learnt how to create tables with constraints, how to optimize queries by adding indexes, implementing stored procedures and functions. I also learnt how to use views and triggers in MySQL.

## Tasks

### 0. We are all unique

Write a SQL script that creates a table `users` following these requirements:

- `id`, integer, never null, auto increment and primary key
- `email`, string (255 characters), never null and unique
- `name`, string (255 characters)

If the table already exists, your script should not fail. Your script can be executed on any database

**File**: [0-uniq_users.sql](./0-uniq_users.sql)

### 1. In and not out

Write a SQL script that creates a table `users` following these requirements:

- `id`, integer, never null, auto increment and primary key
- `email`, string (255 characters), never null and unique
- `name`, string (255 characters)
- `country`, enumeration of countries: `US`, `CO` and `TN`, never null (= default will be the first element of the enumeration, here `US`)

If the table already exists, your script should not fail. Your script can be executed on any database

**File**: [1-country_users.sql](./1-country_users.sql)

### 2. Best band ever

Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

Requirements:

- Import this table dump: *metal_bands.sql.zip*
- Column names must be: `origin` and `nb_fans`
- Your script can be executed on any database

**File**: [2-fans.sql](./2-fans.sql)

### 3. Old school band

Write a SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity

Requirements:

- Import this table dump: *metal_bands.sql.zip*
- Column names must be: `band_name` and `lifespan` (in years)
- You should use attributes `formed` and `split` for computing the `lifespan`
- Your script can be executed on any database

**File**: [3-glam_rock.sql](./3-glam_rock.sql)

### 4. Buy buy buy

Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table `items` can be negative.

**File**: [4-store.sql](./4-store.sql)

### 5. Email validation to sent

Write a SQL script that creates a trigger that resets the `attribute` valid_email only when the `email` has been changed.

**File**: [5-valid_email.sql](./5-valid_email.sql)

### 6. Add bonus

Write a SQL script that creates a stored procedure `AddBonus` that adds a new correction for a student.

Requirements:

- Procedure `AddBonus` is taking 3 inputs (in this order):
- `user_id`, a `users.id` value (you can assume user_id is linked to an existing `users`)
- `project_name`, a new or already exists `projects` - if no `projects.name` found in the table, you should create it
- `score`, the score value for the correction

**File**: [6-bonus.sql](./6-bonus.sql)

### 7. Average score

Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` that computes and store the average score for a student. Note: An average score can be a decimal

Requirements:

- Procedure `ComputeAverageScoreForUser` is taking 1 input:
  - `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)

**File**: [7-average_score.sql](./7-average_score.sql)

### 8. Optimize simple search

Write a SQL script that creates an index `idx_name_first` on the table `names` and the first letter of `name`.

Requirements:

- Import this table dump: *names.sql.zip*
- Only the first letter of `name` must be indexed

**File**: [8-index_my_names.sql](./8-index_my_names.sql)

### 9. Optimize search and score

Write a SQL script that creates an index `idx_name_first_score` on the table `names` and the first letter of `name` and the `score`.

Requirements:

- Import this table dump: *names.sql.zip*
- Only the first letter of `name` AND `score` must be indexed

**File**: [9-index_name_score.sql](./9-index_name_score.sql)

### 10. Safe divide

Write a SQL script that creates a function `SafeDiv` that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

Requirements:

- You must create a function
- The function `SafeDiv` takes 2 arguments:
  - `a`, INT
  - `b`, INT
- And returns `a / b` or 0 if `b == 0`

**File**: [10-div.sql](./10-div.sql)

### 11. No table for a meeting

Write a SQL script that creates a view `need_meeting` that lists all students that have a score under 80 (strict) and no `last_meeting` or more than 1 month.

Requirements:

- The view `need_meeting` should return all students name when:
  - They score are under (strict) to 80
  - **AND** no `last_meeting` date **OR** more than a month

**File**: [11-need_meeting.sql](./11-need_meeting.sql)
-- Optimize search and score
CREATE INDEX idx_name_first_score on names (name(1), score(1))
-- Optimize search and score
CREATE INDEX idx_name_first_score on names (
  name(1)
  AND score(1)
)
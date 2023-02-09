-- Rank country origins of bands ordered by number of non-unique fans
SELECT origin,
  fans AS nb_fans
FROM metal_bands
ORDER BY DISTINCT fans
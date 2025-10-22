# Write your MySQL query statement below
SELECT 
    sample_id,
    dna_sequence,
    species,
    -- Starts with 'ATG'
    CASE 
        WHEN dna_sequence LIKE 'ATG%' THEN 1 
        ELSE 0 
    END AS has_start,

    -- Ends with 'TAA', 'TAG', or 'TGA'
    CASE 
        WHEN dna_sequence LIKE '%TAA' 
          OR dna_sequence LIKE '%TAG' 
          OR dna_sequence LIKE '%TGA' THEN 1
        ELSE 0 
    END AS has_stop,

    -- Contains the motif 'ATAT'
    CASE 
        WHEN dna_sequence LIKE '%ATAT%' THEN 1 
        ELSE 0 
    END AS has_atat,

    -- Contains 3 or more consecutive 'G's
    CASE 
        WHEN dna_sequence REGEXP 'GGG+' THEN 1 
        ELSE 0 
    END AS has_ggg

FROM Samples
ORDER BY sample_id ASC;

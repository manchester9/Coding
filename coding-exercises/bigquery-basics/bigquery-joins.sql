#standardSQL
WITH
  --
  -- Retrieve the variants in this cohort, flattening by alternate bases and
  -- counting affected alleles.
  variants AS (
  SELECT
    REPLACE(reference_name, 'chr', '') as reference_name,
    start_position,
    end_position,
    reference_bases,
    alternate_bases.alt AS alt,
    (SELECT COUNTIF(gt = alt_offset+1) FROM v.call call, call.genotype gt) AS num_variant_alleles,
    (SELECT COUNTIF(gt >= 0) FROM v.call call, call.genotype gt) AS total_num_alleles
  FROM
    `bigquery-public-data.human_genome_variants.platinum_genomes_deepvariant_variants_20180823` v,
    UNNEST(v.alternate_bases) alternate_bases WITH OFFSET alt_offset ),
  --
  -- Define an inline table that uses five rows
  -- selected from silver-wall-555.TuteTable.hg19.
  intervals AS (
    SELECT * FROM UNNEST ([
    STRUCT<Gene STRING, Chr STRING, gene_start INT64, gene_end INT64, region_start INT64, region_end INT64>
    ('PRCC', '1', 156736274, 156771607, 156636274, 156871607),
    ('NTRK1', '1', 156785541, 156852640, 156685541, 156952640),
    ('PAX8', '2', 113972574, 114037496, 113872574, 114137496),
    ('FHIT', '3', 59734036, 61238131, 59634036, 61338131),
    ('PPARG', '3', 12328349, 12476853, 12228349, 12576853)
  ])),
  --
  -- JOIN the variants with the genomic intervals overlapping
  -- the genes of interest.
  --
  -- The JOIN criteria is complicated because the task is to see if
  -- an SNP overlaps an interval.  With standard SQL you can use complex
  -- JOIN predicates, including arbitrary expressions.
  gene_variants AS (
  SELECT
    reference_name,
    start_position,
    reference_bases,
    alt,
    num_variant_alleles,
    total_num_alleles
  FROM
    variants
  INNER JOIN
    intervals ON
    variants.reference_name = intervals.Chr
    AND intervals.region_start <= variants.start_position
    AND intervals.region_end >= variants.end_position )
  --
  -- And finally JOIN the variants in the regions of interest
  -- with annotations for rare variants.
SELECT DISTINCT
  Chr,
  annots.Start AS Start,
  Ref,
  annots.Alt,
  Func,
  Gene,
  PopFreqMax,
  ExonicFunc,
  num_variant_alleles,
  total_num_alleles
FROM
  `silver-wall-555.TuteTable.hg19` AS annots
INNER JOIN
  gene_variants AS vars
ON
  vars.reference_name = annots.Chr
  AND vars.start_position = annots.Start
  AND vars.reference_bases = annots.Ref
  AND vars.alt = annots.Alt
WHERE
  -- Retrieve annotations for rare variants only.
  PopFreqMax <= 0.01
ORDER BY
  Chr,
  Start;
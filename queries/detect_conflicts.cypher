MATCH
    (d1:Document)-[:CONTAINS]->(f1:Fact)-[:REFERS_TO]->(e:Event),
    (d2:Document)-[:CONTAINS]->(f2:Fact)-[:REFERS_TO]->(e)
WHERE
    id(d1) < id(d2)
    AND f1.date <> f2.date
RETURN
    e.name AS event,
    d1.name AS document1,
    f1.date AS date1,
    d2.name AS document2,
    f2.date AS date2 
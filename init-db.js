db = db.getSiblingDB("interview");
db.employee.drop();
db.candidate.drop();
db.schedule.drop();

db.employee.insertMany([
  {
    e_id: 1,
    e_name: "Selva",
  },
  {
    e_id: 2,
    e_name: "Ramu",
  },
  {
    e_id: 3,
    e_name: "Sai",
  },
]);

db.candidate.insertMany([
  {
    c_id: 1,
    c_name: "Shankar",
  },
  {
    c_id: 2,
    c_name: "Thiru",
  },
  {
    c_id: 3,
    c_name: "Bala",
  },
]);

db.schedule.insertMany([
  {
    interview_id: 1,
    candidate: 1,
    employees: [1, 2],
    date: new Date("2023-02-14").toISOString(),
    slot: 1,
    status: false,
  },
]);

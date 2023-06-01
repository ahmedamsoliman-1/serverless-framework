const Responses = require("../common/API_Responses");
const Dynamo = require("../common/Dynamo");

require("dotenv").config();

const tableName = process.env.tableName;

exports.handler = async (event) => {
  console.log("Event ", event);

  const { connectionId: connectionID } = event.requestContext;

  await Dynamo.delete(connectionID, tableName);

  return Responses._200({ message: "disconnected" });
};

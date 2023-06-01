const Response = require("../common/API_Responses");
const AWS = require("aws-sdk");

exports.handler = async (event) => {
  const body = JSON.parse(event.body);

  if (!body) {
    return Response._400({ message: "no text field on the body -_-" });
  }
};

const Responses = require("../common/API_Responses");
const AWS = require("aws-sdk");

const SNS = new AWS.SNS({ apiVersion: "2010-03-31" });

exports.handler = async (event) => {
  console.log("event: " + JSON.stringify(event));

  const body = JSON.parse(event.body);

  if (!body || !body.phoneNumber || !body.message) {
    return Responses._400({ message: "Missing required fields" });
  }

  const AttributParams = {
    attributes: {
      DefaultSMSType: "Promotional",
    },
  };

  const messageParams = {
    Message: body.message,
    PhoneNumber: body.phoneNumber,
  };

  try {
    await SNS.setSMSAttributes(AttributParams).promise();
    await SNS.publish(messageParams).promise();
    return Responses._200({ message: "Message sent" });
  } catch (error) {
    console.log("error: " + error);
    return Responses._400({ message: "Message not sent" });
  }
};

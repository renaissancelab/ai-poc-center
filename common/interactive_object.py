class InteractiveMessage(object):
    id: int
    userId: str
    chatId: str
    bot: str
    photoResourceId: int
    photoUrl: str
    videoResourceId: int
    videoUrl: str
    compositeVideoUrl: str
    status: int
    result: str
    createTime: int
    updateTime: int
    platformType: str
    timeCost: int

    def __init__(self, interactive):
        self.id = interactive["id"]
        self.userId = interactive["userId"]
        self.bot = interactive["bot"]
        if "chatId" in interactive:
            self.chatId = interactive["chatId"]
        if "photoResourceId" in interactive:
            self.photoResourceId = interactive["photoResourceId"]
        if "videoResourceId" in interactive:
            self.videoResourceId = interactive["videoResourceId"]
        self.photoUrl = interactive["photoUrl"]
        self.videoUrl = interactive["videoUrl"]
        if "compositeVideoUrl" in interactive:
            self.compositeVideoUrl = interactive["compositeVideoUrl"]
        else:
            self.compositeVideoUrl = ""
        if "timeCost" in interactive:
            self.timeCost = interactive["timeCost"]
        else:
            self.timeCost = 0
        self.status = interactive["status"]
        self.result = interactive["result"]
        self.createTime = interactive["createTime"]
        self.updateTime = interactive["updateTime"]
        self.platformType = interactive["platformType"]

    def serialize(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'chatId': self.chatId,
            'bot': self.bot,
            'photoUrl': self.photoUrl,
            'videoUrl': self.videoUrl,
            'compositeVideoUrl': self.compositeVideoUrl,
            'status': self.status,
            'result': self.result,
            'createTime': self.createTime,
            'updateTime': self.updateTime,
            'platformType': self.platformType,
            'timeCost': self.timeCost,
        }


def obj_to_dict(interactive_message_obj) -> dict:
    interactive_message_dict = {}
    interactive_message_dict['id'] = interactive_message_obj.id
    interactive_message_dict['userId'] = interactive_message_obj.userId
    interactive_message_dict['bot'] = interactive_message_obj.bot
    interactive_message_dict['photoUrl'] = interactive_message_obj.photoUrl
    interactive_message_dict['videoUrl'] = interactive_message_obj.videoUrl
    if hasattr(interactive_message_obj, "chatId"):
        interactive_message_dict['chatId'] = interactive_message_obj.chatId
    if hasattr(interactive_message_obj, "photoResourceId"):
        interactive_message_dict['photoResourceId'] = interactive_message_obj.photoResourceId
    if hasattr(interactive_message_obj, "videoResourceId"):
        interactive_message_dict['videoResourceId'] = interactive_message_obj.videoResourceId
    if hasattr(interactive_message_obj, "compositeVideoUrl"):
        interactive_message_dict['compositeVideoUrl'] = interactive_message_obj.compositeVideoUrl
    if hasattr(interactive_message_obj, "result"):
        interactive_message_dict['result'] = interactive_message_obj.result
    interactive_message_dict['status'] = interactive_message_obj.status
    interactive_message_dict['createTime'] = interactive_message_obj.createTime
    interactive_message_dict['updateTime'] = interactive_message_obj.updateTime
    interactive_message_dict['platformType'] = interactive_message_obj.platformType
    interactive_message_dict['timeCost'] = interactive_message_obj.timeCost


    return interactive_message_dict

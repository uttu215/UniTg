from sample_config import Config

class Development(Config):
  APP_ID = 928403
  API_HASH = "4a546388b91f6f815c4a6adbbc30d574"
  TG_BOT_TOKEN_BF_HER = ""
  TG_BOT_USER_NAME_BF_HER = ""
  UB_BLACK_LIST_CHAT = []
  # chat ids or usernames, it is recommended to use chat ids,
  # providing usernames means an additional overhead for the user
  CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
  # specify LOAD and NO_LOAD
  LOAD = []
  NO_LOAD = []

  const MODE = "viewsets";  // "api", "generics", "mixin_generics", "viewsets"

  // 자동 URL 설정 객체
  const ENDPOINTS = {
    api: {
      BASE_URL: "/todo/api/",
      list: "list/",
      create: "create/",
      retrieve: "retrieve/",
      update: "update/",
      delete: "delete/"
    },
    generics: {
      BASE_URL: "/todo/generics/",
      list: "list/",
      create: "create/",
      retrieve: "retrieve/",
      update: "update/",
      delete: "delete/"
    },
    mixin_generics: {
      BASE_URL: "/todo/mixin_generics/",
      list: "",  // == BASE_URL
      create: "",
      retrieve: "",
      update: "",
      delete: ""
    },
    viewsets: {
      BASE_URL: "/todo/viewsets/",
      list: "",
      create: "",
      retrieve: "",
      update: "",
      delete: ""
    }
  };

  // 현재 MODE에 맞는 설정 가져오기
  const config = ENDPOINTS[MODE];

  // 그대로 변수에 할당 (원래 변수명 유지)
  const TODO_API_LIST_URL     = config.BASE_URL + config.list;
  const TODO_API_CREATE_URL   = config.BASE_URL + config.create;
  const TODO_API_RETRIEVE_URL = config.BASE_URL + config.retrieve;
  const TODO_API_UPDATE_URL   = config.BASE_URL + config.update;
  const TODO_API_DELETE_URL   = config.BASE_URL + config.delete;

  // 동적 ID 붙일 함수 (예: /1/)
//   const getRetrieveUrl = pk => TODO_API_RETRIEVE_URL + pk + "/";
//   const getUpdateUrl   = pk => TODO_API_UPDATE_URL   + pk + "/";
//   const getDeleteUrl   = pk => TODO_API_DELETE_URL   + pk + "/";

  // 예시 출력
  console.log("TODO_API_LIST_URL:", TODO_API_LIST_URL);
  console.log("TODO_API_CREATE_URL:", TODO_API_CREATE_URL);
  console.log("TODO_API_RETRIEVE_URL:", TODO_API_RETRIEVE_URL);
  console.log("TODO_API_UPDATE_URL:", TODO_API_UPDATE_URL);
  console.log("TODO_API_DELETE_URL:", TODO_API_DELETE_URL);
  


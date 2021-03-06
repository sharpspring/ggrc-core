/*
    Copyright (C) 2019 Google Inc.
    Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
*/

function Proxy(optionModelName, joinOptionAttr, joinModelName,
  joinObjectAttr, instanceJoinAttr) {
  return new GGRC.ListLoaders.ProxyListLoader(
    joinModelName, joinObjectAttr, joinOptionAttr,
    instanceJoinAttr, optionModelName);
}

function Direct(
  optionModelName, instanceJoinAttr, remoteJoinAttr) {
  return new GGRC.ListLoaders.DirectListLoader(
    optionModelName, instanceJoinAttr, remoteJoinAttr);
}

function Search(queryFunction, observeTypes) {
  return new GGRC.ListLoaders.SearchListLoader(queryFunction, observeTypes);
}

function Multi(sources) {
  return new GGRC.ListLoaders.MultiListLoader(sources);
}

function CustomFilter(source, filterFn) {
  return new GGRC.ListLoaders.CustomFilteredListLoader(source, filterFn);
}

export {
  Proxy,
  Direct,
  Search,
  Multi,
  CustomFilter,
};


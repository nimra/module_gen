(window.webpackJsonp=window.webpackJsonp||[]).push([[72],{2731:function(e,r,a){"use strict";a.r(r);var t=a(1),n=a.n(t),o=a(0),i=a(11),d=a(99),s=a(2),c=a(242),u=a(250),l=a.n(u),g=a(114),f=a(744),m=a(85),p=a(249),b=a(1368);function y(){return(y=Object.assign||function(e){for(var r=1;r<arguments.length;r++){var a=arguments[r];for(var t in a)Object.prototype.hasOwnProperty.call(a,t)&&(e[t]=a[t])}return e}).apply(this,arguments)}function k(e,r){return function(e){if(Array.isArray(e))return e}(e)||function(e,r){var a=[],t=!0,n=!1,o=void 0;try{for(var i,d=e[Symbol.iterator]();!(t=(i=d.next()).done)&&(a.push(i.value),!r||a.length!==r);t=!0);}catch(e){n=!0,o=e}finally{try{t||null==d.return||d.return()}finally{if(n)throw o}}return a}(e,r)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()}function x(e){var r=e.currentPage,a=e.pageCount,t=e.onNext,i=e.onBack,d=r<a-1,s=r>0;return o.createElement("div",{className:"jsx-1336833980 tutorials-nav"},o.createElement("a",{onClick:s?i:void 0,className:"jsx-1336833980 "+((s?"":"hide")||"")},"< prev"),o.createElement("span",{className:"jsx-1336833980"},"Page ",r+1," / ",a),o.createElement("a",{onClick:d?t:void 0,className:"jsx-1336833980 "+((d?"":"hide")||"")},"next >"),o.createElement(n.a,{id:"1336833980"},[".tutorials-nav.jsx-1336833980{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-box-pack:justify;-webkit-justify-content:space-between;-ms-flex-pack:justify;justify-content:space-between;background:rgba(0,0,0,0.2);padding:10px;padding-right:15px;min-height:40px;}",".hide.jsx-1336833980{opacity:0;cursor:default;}"]))}var B=function(e){var r=e.wid,a=e.theme,t=e.post,d=e.currentPage,u=e.isAnon,B=o.useRef(null),h=k(o.useState(u),2),w=h[0],v=h[1],E=k(o.useState(null),2),_=E[0],j=E[1];o.useEffect(function(){return j(setTimeout(e.trackLongUsage,3e5)),function(){_&&clearInterval(_)}},[]);var I=Object(i.e)(),S=s.a[a];return o.useEffect(function(){B&&B.current&&(B.current.scrollTop=0)},[d]),o.createElement("div",{ref:B,className:n.a.dynamic([["1057576384",[S.base.foreground]]])+" tutorial-post-wrapper"},o.createElement(f.a,{title:"Build Projects on Repl.it",description:"Please sign up/log in to view the rest of the tutorial",allowAnon:!1,onSuccess:function(){return v(!1)}}),o.createElement(x,{currentPage:d,pageCount:t.tutorialPages.length,onNext:function(){I(w?Object(m.e)():{type:"TUTORIAL_NEXT_PAGE",wid:r})},onBack:function(){I({type:"TUTORIAL_PREVIOUS_PAGE",wid:r})}}),o.createElement("div",{className:n.a.dynamic([["1057576384",[S.base.foreground]]])+" rendered-markdown"},o.createElement(c.a,{theme:a,source:t.tutorialPages[d],className:"content",renderers:{code:function(e){return o.createElement(b.a,y({},e,{theme:a}))},linkReference:g.c,image:g.b},plugins:[p.markdownMentionPlugin,l.a]})),o.createElement(n.a,{id:"1057576384",dynamic:[S.base.foreground]},[".tutorial-post-wrapper.__jsx-style-dynamic-selector{color:".concat(S.base.foreground,";position:relative;-webkit-flex:1;-ms-flex:1;flex:1;min-height:0;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}"),".rendered-markdown.__jsx-style-dynamic-selector{overflow:scroll;-webkit-flex:1;-ms-flex:1;flex:1;min-height:0;padding:10px;padding-right:15px;}"]))},h=a(6),w=a(23),v=a(13),E=a(16);function _(e){return function(e){if(Array.isArray(e)){for(var r=0,a=new Array(e.length);r<e.length;r++)a[r]=e[r];return a}}(e)||function(e){if(Symbol.iterator in Object(e)||"[object Arguments]"===Object.prototype.toString.call(e))return Array.from(e)}(e)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance")}()}var j=17;r.default=Object(i.c)(function(e,r){var a=Object(v.a)(e,r.wid,r.pud,"tutorials").repl;return{isAnon:!(e.user&&e.user.userInfo&&e.user.userInfo.id),replId:a.id,language:a.language,userId:e.user.userInfo&&e.user.userInfo.id}})(function(e){var r=e.theme,a=e.language,t=e.userId,c=e.replId,u=e.wid,l=e.pud,g=e.isAnon,f=s.a[r],m=Object(i.e)(),p=Object(i.f)(function(e){return Object(v.a)(e,u,l,"tutorials")}),b=p.currentPage,y=p.currentTutorialId;o.useEffect(function(){Object(h.track)(h.events.REPL_TUTORIAL_PANE_OPENED,{userId:t})},[]);var k=function(e){m({type:"SELECT_TUTORIAL",wid:u,tutorialId:e}),e&&Object(h.track)(h.events.REPL_TUTORIAL_TUTORIAL_CLICKED,{postId:e,language:a})};return o.createElement("div",{className:n.a.dynamic([["2034145150",[f.sideBar.foreground,f.sideBar.background,f.sideBarSectionHeader.foreground,f.sideBarSectionHeader.background,f.base.foreground,f.list.hoverBackground,f.sideBar.foreground,f.sideBar.background]]])+" tutorials-pane"},o.createElement(d.a,null),o.createElement("div",{className:n.a.dynamic([["2034145150",[f.sideBar.foreground,f.sideBar.background,f.sideBarSectionHeader.foreground,f.sideBarSectionHeader.background,f.base.foreground,f.list.hoverBackground,f.sideBar.foreground,f.sideBar.background]]])+" header"},y?o.createElement("a",{onClick:function(){return k(null)},className:n.a.dynamic([["2034145150",[f.sideBar.foreground,f.sideBar.background,f.sideBarSectionHeader.foreground,f.sideBarSectionHeader.background,f.base.foreground,f.list.hoverBackground,f.sideBar.foreground,f.sideBar.background]]])},"◀ back to tutorials"):"Community Tutorials"),o.createElement(E.u,{variables:{id:j,postsOrder:"votes",languages:[a]}},function(e){var i=e.loading,d=e.data;if(i)return o.createElement("div",{className:n.a.dynamic([["2034145150",[f.sideBar.foreground,f.sideBar.background,f.sideBarSectionHeader.foreground,f.sideBarSectionHeader.background,f.base.foreground,f.list.hoverBackground,f.sideBar.foreground,f.sideBar.background]]])+" loader-wrapper"},o.createElement(w.a,null));var s=[];if(d&&d.postsByBoard&&d.postsByBoard.items&&s.push.apply(s,_(d.postsByBoard.items)),y){var l=s.find(function(e){return e.id===y});return o.createElement(B,{theme:r,post:l,currentPage:b,trackLongUsage:function(){Object(h.track)(h.events.REPL_TUTORIAL_5M_ELAPSED,{userId:t,language:a,postId:l.id,replId:c})},wid:u,isAnon:g})}return o.createElement("div",{className:n.a.dynamic([["2034145150",[f.sideBar.foreground,f.sideBar.background,f.sideBarSectionHeader.foreground,f.sideBarSectionHeader.background,f.base.foreground,f.list.hoverBackground,f.sideBar.foreground,f.sideBar.background]]])+" tutorials-wrapper"},s.map(function(e){return o.createElement(o.Fragment,null,o.createElement("div",{key:"post-tutorial-".concat(e.id),onClick:function(){return k(e.id)},className:n.a.dynamic([["2034145150",[f.sideBar.foreground,f.sideBar.background,f.sideBarSectionHeader.foreground,f.sideBarSectionHeader.background,f.base.foreground,f.list.hoverBackground,f.sideBar.foreground,f.sideBar.background]]])+" tutorial-item"},o.createElement("div",{title:e.title,className:n.a.dynamic([["2034145150",[f.sideBar.foreground,f.sideBar.background,f.sideBarSectionHeader.foreground,f.sideBarSectionHeader.background,f.base.foreground,f.list.hoverBackground,f.sideBar.foreground,f.sideBar.background]]])+" title"},e.title),o.createElement("div",{className:n.a.dynamic([["2034145150",[f.sideBar.foreground,f.sideBar.background,f.sideBarSectionHeader.foreground,f.sideBarSectionHeader.background,f.base.foreground,f.list.hoverBackground,f.sideBar.foreground,f.sideBar.background]]])+" author"},"By",o.createElement("img",{src:e.user.image,className:n.a.dynamic([["2034145150",[f.sideBar.foreground,f.sideBar.background,f.sideBarSectionHeader.foreground,f.sideBarSectionHeader.background,f.base.foreground,f.list.hoverBackground,f.sideBar.foreground,f.sideBar.background]]])}),e.user.username)),o.createElement("div",{className:n.a.dynamic([["2034145150",[f.sideBar.foreground,f.sideBar.background,f.sideBarSectionHeader.foreground,f.sideBarSectionHeader.background,f.base.foreground,f.list.hoverBackground,f.sideBar.foreground,f.sideBar.background]]])+" tutorial-border"}))}),0===s.length&&o.createElement("div",{className:n.a.dynamic([["2034145150",[f.sideBar.foreground,f.sideBar.background,f.sideBarSectionHeader.foreground,f.sideBarSectionHeader.background,f.base.foreground,f.list.hoverBackground,f.sideBar.foreground,f.sideBar.background]]])+" posts-empty-message"},"No tutorials found"),o.createElement("a",{href:"/talk/learn",target:"_blank",onClick:function(){return Object(h.track)(h.events.REPL_TUTORIAL_BOARD_LINK_CLICKED,{userId:t})},className:n.a.dynamic([["2034145150",[f.sideBar.foreground,f.sideBar.background,f.sideBarSectionHeader.foreground,f.sideBarSectionHeader.background,f.base.foreground,f.list.hoverBackground,f.sideBar.foreground,f.sideBar.background]]])+" tutorial-item"},"Want to add your own? Write one here!"))}),o.createElement(n.a,{id:"2034145150",dynamic:[f.sideBar.foreground,f.sideBar.background,f.sideBarSectionHeader.foreground,f.sideBarSectionHeader.background,f.base.foreground,f.list.hoverBackground,f.sideBar.foreground,f.sideBar.background]},[".tutorials-pane.__jsx-style-dynamic-selector{height:100%;color:".concat(f.sideBar.foreground,";background:").concat(f.sideBar.background,";display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;}"),".tutorials-wrapper.__jsx-style-dynamic-selector{font-family:Questrial;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-direction:column;-ms-flex-direction:column;flex-direction:column;overflow:auto;max-height:100vh;padding-bottom:200px;}",".header.__jsx-style-dynamic-selector{font-size:16px;width:100%;min-height:43px;padding:4px 10px 8px 10px;text-align:center;color:".concat(f.sideBarSectionHeader.foreground,";background:").concat(f.sideBarSectionHeader.background,";}"),".posts-empty-message.__jsx-style-dynamic-selector{text-align:center;padding:20px 10px;}",".tutorial-item.__jsx-style-dynamic-selector{padding:20px 10px;cursor:pointer;}",".tutorial-border.__jsx-style-dynamic-selector{width:50%;margin:0 auto;height:1px;border-bottom:1px solid ".concat(f.base.foreground,";}"),".tutorial-item.__jsx-style-dynamic-selector .title.__jsx-style-dynamic-selector{width:100%;text-overflow:ellipsis;overflow:hidden;white-space:nowrap;}",".tutorial-item.__jsx-style-dynamic-selector .author.__jsx-style-dynamic-selector{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;width:100%;overflow:hidden;margin-top:5px;font-size:14px;}",".tutorial-item.__jsx-style-dynamic-selector img.__jsx-style-dynamic-selector{width:20px;height:20px;border-radius:10px;margin:0 4px;}",".tutorial-item.__jsx-style-dynamic-selector:hover{background:".concat(f.list.hoverBackground,";}"),"a.__jsx-style-dynamic-selector{color:".concat(f.sideBar.foreground,";border-bottom:none;}"),".loader-wrapper.__jsx-style-dynamic-selector{margin-top:30px;display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;-ms-flex-pack:center;justify-content:center;-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;background:".concat(f.sideBar.background,";}")]))})},744:function(e,r,a){"use strict";var t=a(0),n=a(11),o=a(170),i=a(35),d=a(85);function s(e,r){if(null==e)return{};var a,t,n=function(e,r){if(null==e)return{};var a,t,n={},o=Object.keys(e);for(t=0;t<o.length;t++)a=o[t],r.indexOf(a)>=0||(n[a]=e[a]);return n}(e,r);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(t=0;t<o.length;t++)a=o[t],r.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(n[a]=e[a])}return n}var c=function(e){var r=e.promptCount,a=e.promptCountThreshold,n=e.dismissed,d=e.show,c=e.hideModal,u=e.dismiss,l=e.isLoggedIn,g=s(e,["promptCount","promptCountThreshold","dismissed","show","hideModal","dismiss","isLoggedIn"]);return l||!(d||r>=a)||n?null:t.createElement(i.a,{hideModal:function(){u(),c&&c()}},t.createElement(o.a,g))};c.defaultProps={promptCountThreshold:5},r.a=Object(n.c)(function(e){return{isLoggedIn:e.user.userInfo.isLoggedIn,show:!e.user.userInfo.isLoggedIn&&e.user.authModal.show,promptCount:e.user.authModal.promptCount,dismissed:e.user.authModal.dismissed}},{dismiss:d.b})(c)}}]);
//# sourceMappingURL=72.18be004592c18a4e2ba8.js.map
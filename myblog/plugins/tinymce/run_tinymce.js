tinyMCE.init({
  mode : 'textareas',
  theme : 'advanced',
  plugins : 'lists,table,template,wordcount',

  theme_advanced_buttons1 : 'cut,copy,paste,pastetext,pasteword,undo,redo,|,formatselect,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,bullist,numlist,blockquote,sub,sup',
  theme_advanced_buttons2 : 'link,unlink,image,code,|,tablecontrols,|,hr,|,removeformat',
  theme_advanced_toolbar_location : "top",
  theme_advanced_toolbar_align : "left",
  theme_advanced_statusbar_location : "bottom",
  theme_advanced_resizing : false,

  template_external_list_url : "lists/template_list.js",
  external_link_list_url : "lists/link_list.js",
  external_image_list_url : "lists/image_list.js",
  media_external_list_url : "lists/media_list.js",
});

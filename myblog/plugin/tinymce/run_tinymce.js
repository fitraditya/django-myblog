tinyMCE.init({
  mode : 'textareas',
  theme : 'advanced',
  plugins : 'lists,table,template,wordcount',

  theme_advanced_buttons1 : 'cut,copy,paste,pastetext,pasteword,undo,redo,|,formatselect,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,bullist,numlist,blockquote,sub,sup',
  theme_advanced_buttons2 : 'link,unlink,image,code,|,tablecontrols,|,hr,|,removeformat',
  theme_advanced_toolbar_location : "top",
  theme_advanced_toolbar_align : "left",
  theme_advanced_statusbar_location : "bottom",
  theme_advanced_resizing : true,

  template_external_list_url : "lists/template_list.js",
  external_link_list_url : "lists/link_list.js",
  external_image_list_url : "lists/image_list.js",
  media_external_list_url : "lists/media_list.js",

  style_formats : [
    {title : 'Bold text', inline : 'b'},
    {title : 'Red text', inline : 'span', styles : {color : '#ff0000'}},
    {title : 'Red header', block : 'h1', styles : {color : '#ff0000'}},
    {title : 'Example 1', inline : 'span', classes : 'example1'},
    {title : 'Example 2', inline : 'span', classes : 'example2'},
    {title : 'Table styles'},
    {title : 'Table row 1', selector : 'tr', classes : 'tablerow1'}
  ],

  formats : {
    alignleft : {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'left'},
    aligncenter : {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'center'},
    alignright : {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'right'},
    alignfull : {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'full'},
    bold : {inline : 'span', 'classes' : 'bold'},
    italic : {inline : 'span', 'classes' : 'italic'},
    underline : {inline : 'span', 'classes' : 'underline', exact : true},
    strikethrough : {inline : 'del'}
  },
});

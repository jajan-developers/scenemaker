(function ($, window) {

    $.fn.contextMenu = function (settings) {

        return this.each(function () {

            // Open context menu
            $(this).on("contextmenu", function (e) {
                //open menu
                $(settings.menuSelector)
                    .data("invokedOn", $(e.target))
                    .show()
                    .css({
                        position: "absolute",
                        left: getLeftLocation(e),
                        top: getTopLocation(e)
                    })
                    .off('click')
                    .on('click', function (e) {
                        $(this).hide();
                
                        var $invokedOn = $(this).data("invokedOn");
                        var $selectedMenu = $(e.target);
                        
                        settings.menuSelected.call(this, $invokedOn, $selectedMenu);
                });
                
                return false;
            });

            //make sure menu closes on any click
            $(document).click(function () {
                $(settings.menuSelector).hide();
            });
        });

        function getLeftLocation(e) {
            var mouseWidth = e.pageX;
            var pageWidth = $(window).width();
            var menuWidth = $(settings.menuSelector).width();
            
            // opening menu would pass the side of the page
            if (mouseWidth + menuWidth > pageWidth &&
                menuWidth < mouseWidth) {
                return mouseWidth - menuWidth;
            } 
            return mouseWidth;
        }        
        
        function getTopLocation(e) {
            var mouseHeight = e.pageY;
            var pageHeight = $(window).height();
            var menuHeight = $(settings.menuSelector).height();

            // opening menu would pass the bottom of the page
            if (mouseHeight + menuHeight > pageHeight &&
                menuHeight < mouseHeight) {
                return mouseHeight - menuHeight;
            } 
            return mouseHeight;
        }

    };
})(jQuery, window);

// Example
// $("#myTable td").contextMenu({
//     menuSelector: "#contextMenu",
//     menuSelected: function (invokedOn, selectedMenu) {
//         var msg = "You selected the menu item '" + selectedMenu.text() +
//             "' on the value '" + invokedOn.text() + "'";
//         alert(msg);
//     }
// });
// Invoked - Clicked Location w/ .contextMenu jQuery
// SelectedMenu - Item selected on the context menu

// <ul id="contextMenu" class="dropdown-menu" role="menu" style="display:none" >
//     <li><a tabindex="-1" href="#">Action</a></li>
//     <li><a tabindex="-1" href="#">Another action</a></li>
//     <li><a tabindex="-1" href="#">Something else here</a></li>
//     <li class="divider"></li>
//     <li><a tabindex="-1" href="#">Separated link</a></li>
// </ul>
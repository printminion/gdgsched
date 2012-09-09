package gdg.devfest.app.ui;

import android.webkit.WebView;

/**
 * Shows a {@link WebView} with a map of the conference venue.
 */
public class MapFragment extends com.google.android.apps.iosched.ui.MapFragment {
	/**
	 * When specified, will automatically point the map to the requested room.
	 */
	public static final String EXTRA_ROOM = "com.google.android.iosched.extra.ROOM";
	private static final String MAP_JSI_NAME = "MAP_CONTAINER";
	private static final String MAP_URL = "http://ioschedmap.appspot.com/embed.html";

}

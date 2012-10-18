package gdg.devfest.ch.app.ui;

import android.support.v4.app.ListFragment;

/**
 * A {@link ListFragment} showing a list of sessions. This fragment supports
 * multiple-selection using the contextual action bar (on API 11+ devices), and
 * also supports a separate 'activated' state for indicating the
 * currently-opened detail view on tablet devices.
 */
public class SessionsFragment extends
		com.google.android.apps.iosched.ui.SessionsFragment {

	private static final String STATE_SELECTED_ID = "selectedId";

}
